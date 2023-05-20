! Create random larger matrix and vector and compute their product and time needed for the two orders of loops of rows and collums, i.e. i,j and j,i, respectively.
! write results to file type line n, time ij, time ji

program Main
    
    use omp_lib
    implicit none
    
    integer :: i, j, n, len_list
    real*8, allocatable :: A(:,:), x(:), B(:)
    real*8 :: start, finish, time1, time2
    integer*8, allocatable :: N_list(:)

    N_list = [1, 10, 100, 1000, 10000, 15000, 20000, 25000]

    open(unit=1, file='results2.txt', status='unknown', action='write', position='append')

    do len_list = 1, 80

        n = N_list(mod(len_list, 8) + 1)

        allocate(A(n,n))
        allocate(x(n))
        allocate(B(n))
        
        call random_seed()
        call random_number(A)
        call random_number(x)
        
        start = omp_get_wtime()

        do i = 1, n
            B(i) = 0.0
            do j = 1, n
                B(i) = B(i) + A(i,j) * x(j)            
            end do
        end do
        
        finish = omp_get_wtime()
        time1 = finish - start
    
        start = omp_get_wtime()

        do i = 1, n
            B(i) = 0.0
        end do

        do j = 1, n
            do i = 1, n
                B(i) = B(i) + A(i,j) * x(j)            
            end do
        end do

        finish = omp_get_wtime()
        time2 = finish - start

        write(1,*) n, time1, time2
 
        deallocate(A)
        deallocate(x)
        deallocate(B)
    end do
    close(1)
end program Main